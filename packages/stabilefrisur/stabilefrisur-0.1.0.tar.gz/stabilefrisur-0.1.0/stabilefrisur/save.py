import pickle
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def save_object(obj, file_name: str, file_type: str, path: Path | str):
    """
    Save an object to a file in the specified format.

    Args:
        obj: The object to save.
        file_name (str): The name of the file (without extension).
        file_type (str): The file format (pickle, csv, xlsx, svg, png).
        path (Path | str): The directory path where the file will be saved.
    """
    # Ensure the path is a Path object
    path = Path(path) if isinstance(path, str) else path
    path.mkdir(parents=True, exist_ok=True)  # Create directory if it doesn't exist

    # Construct the full file path
    file_path = path / f"{file_name}.{file_type}"

    # Dispatch to the appropriate save function based on file type
    if file_type == "p":
        _save_pickle(obj, file_path)
    elif file_type == "csv":
        _save_csv(obj, file_path)
    elif file_type == "xlsx":
        _save_xlsx(obj, file_path)
    elif file_type == "svg":
        _save_svg(obj, file_path)
    elif file_type == "png":
        _save_png(obj, file_path)
    else:
        raise ValueError(f"Unsupported file type: {file_type}")

def _save_pickle(obj, file_path: Path):
    """Save an object to a pickle file."""
    with open(file_path, "wb") as f:
        pickle.dump(obj, f)

def _save_csv(obj: pd.DataFrame | pd.Series, file_path: Path):
    """Save a pandas DataFrame or Series to a CSV file."""
    if isinstance(obj, (pd.DataFrame, pd.Series)):
        obj.to_csv(file_path, index=False)
    else:
        raise ValueError("CSV export requires a pandas DataFrame or Series.")

def _save_xlsx(obj: pd.DataFrame | pd.Series, file_path: Path):
    """Save a pandas DataFrame or Series to an Excel file."""
    if isinstance(obj, (pd.DataFrame, pd.Series)):
        if isinstance(obj, pd.Series):
            obj = obj.to_frame()  # Convert Series to DataFrame for Excel export
        obj.to_excel(file_path, index=False)
    else:
        raise ValueError("Excel export requires a pandas DataFrame or Series.")

def _save_svg(obj: plt.Figure, file_path: Path):
    """Save a Matplotlib figure to an SVG file."""
    if isinstance(obj, plt.Figure):
        obj.savefig(file_path, format="svg")
    else:
        raise ValueError("SVG export requires a Matplotlib figure.")

def _save_png(obj: plt.Figure, file_path: Path):
    """Save a Matplotlib figure to a PNG file."""
    if isinstance(obj, plt.Figure):
        obj.savefig(file_path, format="png")
    else:
        raise ValueError("PNG export requires a Matplotlib figure.")