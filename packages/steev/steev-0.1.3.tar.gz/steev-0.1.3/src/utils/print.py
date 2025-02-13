import sys
import time
from typing import Literal, Optional

import click


def print_line(
    new_line_direction: Literal["up", "down", "both", "none"],
    line_length: int = 40,
) -> None:
    if new_line_direction == "both":
        click.echo("\n" + "─" * line_length + "\n")
    elif new_line_direction == "up":
        click.echo("\n" + "─" * line_length)
    elif new_line_direction == "down":
        click.echo("─" * line_length + "\n")


def typing_print(
    text: str, delay: float = 0.01, color: Optional[str] = None, keywords: Optional[list[str]] = None
) -> None:
    if delay > 0:
        if keywords:
            for keyword in keywords:
                text = text.replace(keyword, click.style(keyword, fg=color))
            for char in text:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(delay)
            sys.stdout.write("\n")
    else:
        click.echo(click.style(text, fg=color), err=True)


def typing_prompt(
    text: str,
    default: Optional[str] = None,
    type=None,
    delay: float = 0.01,
    color: Optional[str] = None,
    keywords: Optional[list[str]] = None,
) -> str:
    # First display the prompt text with typing effect
    if keywords:
        for keyword in keywords:
            text = text.replace(keyword, click.style(keyword, fg=color))

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

    # Modify the default value display format
    if default is not None:
        default_display = f"[{default.upper()}/n]" if default.lower() == "y" else "[y/N]"
        sys.stdout.write(f" {default_display}")

    sys.stdout.write(": ")  # Add the prompt colon
    sys.stdout.flush()

    # Get user input and validate
    while True:
        value = input()
        if not value and default is not None:
            return default
        if type == click.Choice(["y", "n"]):
            value = value.lower()
            if value in ["y", "n"]:
                return value
            click.echo("Please enter 'y' or 'n'")
            continue
        return value


def box_print(title: str, messages: list[str], width: int = 50) -> str:
    """Create a box-styled message with title and content.

    Args:
        title: The title to display at the top of the box
        messages: List of message lines to display in the box
        width: Width of the box (default: 50)

    Returns:
        Formatted string with box-styled message
    """
    # Box characters
    TOP_LEFT = "┌"
    TOP_RIGHT = "┐"
    BOTTOM_LEFT = "└"
    BOTTOM_RIGHT = "┘"
    HORIZONTAL = "─"
    VERTICAL = "│"

    # Create box parts
    top_border = f"{TOP_LEFT}{HORIZONTAL * (width-2)}{TOP_RIGHT}\n"
    title_line = f"{VERTICAL} {title.center(width-4)} {VERTICAL}\n"
    separator = f"{VERTICAL} {HORIZONTAL * (width-4)} {VERTICAL}\n"

    # Create message lines
    content = ""
    while len(messages) > 0:
        msg = messages.pop(0)
        if len(msg) > width - 4:
            m = msg[: width - 4]
            messages.insert(0, f"  {msg[width - 2:]}")
        else:
            m = msg
        content += f"{VERTICAL} {m:<{width-4}} {VERTICAL}\n"

    bottom_border = f"{BOTTOM_LEFT}{HORIZONTAL * (width-2)}{BOTTOM_RIGHT}\n"

    # Combine all parts
    return top_border + title_line + separator + content + bottom_border
