# Tile Image Grid

A command-line tool for splitting images into grids and reconstructing them back together.

## Installation

### From PyPI

To install the tool via PyPI, use the following command:

```bash
pip install tile-image-grid
```

### From Source

To install from source, clone the repository and install the package in editable mode:

```bash
git clone https://github.com/passandscore/tile-image-grid.git
cd tile-image-grid
pip install -e .
```

## Usage

The tool provides two main commands for image grid manipulation: **Split** and **Reconstruct**.

### 1. Split Images

Splits an image into a grid of smaller images.

```bash
tile-image-grid split [OPTIONS] INPUT_PATH
```

#### Arguments:
- `INPUT_PATH`: The path to the input image file.

#### Options:
- `-o, --output-dir TEXT`: The output directory for split images (default: `output`).
- `-g, --grid-size INT`: The size of the grid (e.g., `3` for a 3x3 grid) (default: `3`).
- `--help`: Display help information.

#### Examples:

- Split image into a 3x3 grid:

  ```bash
  tile-image-grid split input.jpg -o tiles -g 3
  ```

- Split image into a 4x4 grid with a custom output directory:

  ```bash
  tile-image-grid split input.jpg -o custom_output -g 4
  ```

### 2. Reconstruct Images

Reconstructs a full image from a directory of image tiles.

```bash
tile-image-grid reconstruct [OPTIONS] INPUT_FOLDER OUTPUT_PATH
```

#### Arguments:
- `INPUT_FOLDER`: The directory containing the image tiles.
- `OUTPUT_PATH`: The path where the reconstructed image will be saved.

#### Options:
- `-b, --border-thickness INT`: The thickness of the border in pixels (default: `2`).
- `-c, --border-color INT...`: The border color in RGB format (default: `0 0 0`).
- `--help`: Display help information.

#### Examples:

- Reconstruct image with a 2px border:

  ```bash
  tile-image-grid reconstruct tiles output.jpg -b 2 -c 255 255 255
  ```

- Basic reconstruction without a border:

  ```bash
  tile-image-grid reconstruct tiles output.png
  ```

- Reconstruction with a custom border thickness:

  ```bash
  tile-image-grid reconstruct tiles output.png -b 3
  ```

- Reconstruction with a red border:

  ```bash
  tile-image-grid reconstruct tiles output.png -b 2 -c 255 0 0
  ```

## File Naming Convention

When splitting images, the tool creates files named in the following format:

- `0_0.png` (top-left tile)
- `0_1.png` (top-middle tile)
- `1_0.png` (middle-left tile)

The first number represents the row, and the second number represents the column.

## Requirements

The following dependencies are required:

- Python 3.7 or higher
- Pillow (PIL)
- Click
- PyTorch (for advanced features)

To install the required dependencies, use:

```bash
pip install -r requirements.txt
```

## Common Issues

### 1. Missing Dependencies

If you encounter errors related to missing dependencies, ensure that all required packages are installed:

```bash
pip install -r requirements.txt
```

### 2. Permission Issues

If you face permission errors while saving files, ensure you have write permissions for the specified output directory.

## Contributing

Contributions are welcome! If you would like to contribute, please submit a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.