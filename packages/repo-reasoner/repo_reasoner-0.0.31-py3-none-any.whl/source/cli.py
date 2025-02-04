# The MIT License (MIT)
#
# Copyright (c) 2024 Vakhidov Dzhovidon
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
Cli runner.
"""
import csv
from typing import Optional, Tuple
import typer
from typer.cli import app
from source.github_repository import GitHubRepository
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_gigachat.chat_models import GigaChat
from source import NAME
import os


@app.command()
def filter_unmaintained(
    repositories: str = typer.Option(
        ..., "--repositories", help="Path to the input repositories CSV file."
    ),
    output: str = typer.Option(
        ..., "--output", help="Path to the output CSV file."
    ),
    api_key: str = typer.Option(
        ..., "--key", help="Your API key to access LLM."
    ),
    model: str = typer.Option(
        "GigaChat", "--model", help="Name of Gigachat Model"
    ),
):
    """
    Filter repositories to identify maintained ones.
    """
    try:
        repos = []

        # Read the input CSV file
        with open(repositories, mode="r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                repository = row["full_name"]
                repos.append(repository)

        file_exists = os.path.isfile(output)

        with open(output, mode="a", encoding="utf-8", newline="") as csvfile:
            fieldnames = ["repository", "maintained", "reason"]

            if not file_exists or os.stat(output).st_size == 0:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()

            for repository in repos:
                status, reason = is_maintained(repository, model, api_key)
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow(
                    {
                        "repository": repository,
                        "maintained": status,
                        "reason": reason,
                    }
                )

        typer.echo(f"Filtered repositories written to {output}")

    except Exception as e:
        typer.echo(f"An unexpected error occurred: {e}")


@app.command()
def is_maintained(
    repository: str = typer.Option(
        ..., "--repository", help="GitHub repository name (e.g., 'owner/repo')"
    ),
    model: str = typer.Option(
        "GigaChat", "--model", help="Name of Gigachat Model"
    ),
    api_key: str = typer.Option(
        ..., "--key", help="your api key to access llm"
    ),
) -> Tuple[str, str]:
    """
    Decides whether the repository is maintained or not and provides a reason.
    """
    try:
        # Initialize the GitHubRepository class
        github_repo = GitHubRepository(repository)

        # Fetch repository data
        github_repo.fetch_repository_data()

        # Extract metrics
        metrics = github_repo.get_key_metrics()

        # Log details for debugging
        typer.echo(
            f"Metrics: Stars={metrics.stars}, Forks={metrics.forks}, "
            f"Last Push={metrics.last_push}, "
            f"Open Issues={metrics.open_issues}, "
            f"Archived={metrics.archived}"
        )

        # GigaChat initialization
        llm = GigaChat(
            credentials=api_key,
            scope="GIGACHAT_API_PERS",
            model=str(model),
            verify_ssl_certs=False,
            streaming=False,
        )

        # System message for GigaChat
        system_message = SystemMessage(
            content=(
                "You are an AI assistant that analyzes GitHub repositories"
                " to determine if they are maintained."
                " You will use the following metrics:"
                " stars, forks, last push date, open issues,"
                " and archived status."
                " Your answer must be 2 lines:"
                ' In first line respond with SINGLE word either "yes" or "no"'
                " In the second line provide a very brief reason "
                " for your decision. "
                " Keep the justification under 50 characters."
            )
        )

        # Human message with repository metrics
        user_message = HumanMessage(
            content=(
                f"Here are the repository metrics:\n"
                f"- Stars: {metrics.stars}\n"
                f"- Forks: {metrics.forks}\n"
                f"- Last Push: {metrics.last_push}\n"
                f"- Open Issues: {metrics.open_issues}\n"
                f"- Archived: {metrics.archived}\n\n"
                f"Is the repository maintained? Please provide a reason."
            )
        )

        # GigaChat invocation
        messages = [system_message, user_message]
        response = llm.invoke(messages)

        # Parse response content: Expected format: "yes" or "no" and a reason
        result = response.content.strip().split("\n", 1)
        status = result[0].strip()
        reason = result[1].strip() if len(result) > 1 else "No reason provided"

        # Print the result in a fixed format
        typer.echo(f"Repository: {repository}")
        typer.echo(f"Maintained: {status}")
        typer.echo(f"Reason: {reason}")

        return status, reason

    except ValueError as ve:
        typer.echo(str(ve))
        return "no", "Error occurred"
    except Exception as e:
        typer.echo(f"An unexpected error occurred: {e}")
        return "no", "Error occurred"


# Run it.
@app.callback()
def main(
    # pylint: disable=unused-argument
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        help="Show the application's version and exit.",
        is_eager=True,
    )
) -> None:
    f"""
    {NAME}
    """
    return
