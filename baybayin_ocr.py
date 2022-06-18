"""
    CSC713M - Machine Learning

    AMOGUIS, ADRIEL ISAIAH V.
    FLORES, BENITO MIGUEL IV
    MADRID, GIAN JOSEPH B.

    BAYBAYIN OCR MODEL USING YOLOv5
"""

# Dependency Imports
import argparse

def train(epochs=300, config=None) -> int:

    pass

def main() -> int:
    """Main Function
    
    This function is the main function and insertion point of the program. It can either be called from the command line or from a script.
    Input can be accepted either by CLI arguments or by running the program with no arguments.

    Returns
    -------
    int
        the exit code of the program
    """

    # Parse CLI Arguments
    parser = argparse.ArgumentParser(description="Run the Baybayin OCR Model")

    parser.add_argument("-tr", "--train", help="Train the model with n epochs.", metavar="train", type=int, default=None)

    parser.add_argument("-p", "--predict", help="Predict Baybayin text in a given image.", metavar="predict", type=str, default=None)
    parser.add_argument("-imgp", "--process-image", help="Apply pre-processing on an image.", metavar="imgp", type=str, default=None)

    args = parser.parse_args()

    # Pass to Trainer
    if args.train is not None:
        train(epochs=args.train)


if __name__ == "__main__":
    main()