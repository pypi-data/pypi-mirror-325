import click

from . import DOC_URL

NO_CREDENTIALS = (
    "\nNO CREDENTIALS\n\n"
    "  No credentials found. Please login or sign up.\n"
    "  Run " + click.style("`steev auth login`", fg="green") + " to login or sign up\n"
    "  For more info, visit our documentation: " + click.style(DOC_URL, fg="blue", underline=True)
)


LOGIN_REQUIRED = (
    "\nLOGIN REQUIRED\n\n"
    "  You should login or sign up before using `steev`\n"
    "  Run " + click.style("`steev auth login`", fg="green") + " to login or sign up\n"
    "  For more info, visit our documentation: " + click.style(DOC_URL, fg="blue", underline=True)
)
