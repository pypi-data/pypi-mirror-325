import click
from pathlib import Path
from typing import Optional
import json
from loguru import logger

from sqldeps.llm_parsers import OpenaiExtractor, GroqExtractor, DeepseekExtractor

FRAMEWORK_DEFAULTS = {
    "groq": {"class": GroqExtractor, "model": "llama-3.3-70b-versatile"},
    "openai": {"class": OpenaiExtractor, "model": "gpt-4o"},
    "deepseek": {"class": DeepseekExtractor, "model": "deepseek-chat"},
}


@click.command()
@click.argument("fpath", type=click.Path(exists=True))
@click.option(
    "--framework",type=click.Choice(["groq", "openai", "deepseek"]), default="groq",
    help="LLM framework to use",
)
@click.option(
    "--model", type=str, default=None,
    help="Model name for the selected framework"
)
@click.option(
    "--prompt", type=click.Path(exists=True), default=None,
    help="Path to custom prompt YAML file",
)
@click.option(
    "-r", "--recursive", is_flag=True, default=False,
    help="Recursively scan folder for SQL files",
)
@click.option(
    "--db-match-schema", is_flag=True, default=False,
    help="Match dependencies against database schema",
)
@click.option(
    "--db-target-schemas", type=str, default="public",
    help="Comma-separated list of target schemas to validate against",
)
@click.option(
    "--db-credentials", type=click.Path(exists=True), default=None,
    help="Path to database credentials YAML file",
)
@click.option(
    "-o", "--output", type=click.Path(), default="dependencies.json",
    help="Output file path for extracted dependencies",
)
def main(
    fpath: str,
    framework: str,
    model: Optional[str],
    prompt: Optional[str],
    recursive: bool,
    db_match_schema: bool,
    db_target_schemas: Optional[str],
    db_credentials: Optional[str],
    output: str,
):
    """Extract SQL dependencies from file or folder"""
    try:
        # Initialize extractor
        framework_config = FRAMEWORK_DEFAULTS[framework]
        extractor_class = framework_config["class"]
        model = model or framework_config["model"]

        extractor = extractor_class(
            model=model,
            params={"temperature": 0},
            prompt_path=prompt if prompt else None,
        )

        # Extract dependencies
        path = Path(fpath)
        if path.is_file():
            dependencies = extractor.extract_from_file(path)
            logger.info(f"Extracted dependencies from file: {path}")
        else:
            dependencies = extractor.extract_from_folder(path, recursive=recursive)
            logger.info(f"Extracted dependencies from folder: {path}")

        # Match against database schema if requested
        if db_match_schema:
            schemas = [s.strip() for s in db_target_schemas.split(",")]
            df_matches = extractor.match_database_schema(
                dependencies,
                target_schemas=schemas,
                db_config_path=db_credentials,  # if db_credentials else None
            )

            # Save schema matches to CSV
            matches_output = Path(output).with_suffix(".csv")
            df_matches.to_csv(matches_output, index=False)
            logger.success(f"Saved schema matches to: {matches_output}")
        else:
            # Save dependencies to CSV
            if Path(output).suffix.lower() == ".csv":
                output_path = Path(output)
                dependencies.to_dataframe().to_csv(output_path, index=False)
            # Save dependencies to JSON
            else:
                output_path = Path(output).with_suffix(".json")
                with open(output_path, "w") as f:
                    json.dump(dependencies.to_dict(), f, indent=2)
            logger.success(f"Saved dependencies to: {output_path}")

    except Exception as e:
        logger.error(f"Error: {e}")
        raise click.ClickException(str(e))


if __name__ == "__main__":
    main()
