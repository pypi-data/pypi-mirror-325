"""
Valid file types for reading data in MTTools-Lib.

Need the following variables:
    label (str): Name of the data type
    time (str): Time system of the data
    file_extensions (list): List of valid file extensions
"""


class BaseInstrument:
    """Base class for the instruments."""

    def __init__(self) -> None:
        self._label = "None"
        self._time = "UTC"
        self._file_extensions: list[str] = []
        self._selection_policy = "one"

    @property
    def label(self) -> str:
        """Return the label of the instrument."""
        return self._label

    @property
    def file_extensions(self) -> list[str]:
        """Return the list of valid file extensions."""
        return self._file_extensions

    @property
    def selection_policy(self) -> str:
        """Return the selection policy."""
        return self._selection_policy


class Dart(BaseInstrument):
    """Class defining the DART instrument."""

    def __init__(self) -> None:
        super().__init__()
        self._label = "DART"
        self._file_extensions = ["DRT", "DART"]


class Nims(BaseInstrument):
    """Class defining the NIMS instrument."""

    def __init__(self) -> None:
        super().__init__()
        self._label = "NIMS"
        self._file_extensions = ["BIN", "NIM"]


class Zen(BaseInstrument):
    """Class defining the Zen instrument."""

    def __init__(self) -> None:
        super().__init__()
        self._label = "Zen"
        self._time = "GNSS"
        self._file_extensions = ["Z3D"]
        self._selection_policy = "many"


# Add a custom type of Nims | Zen to the Controller class
# so that the type hinting is correct.
Instrument = BaseInstrument


class Controller:
    """Class controller for the instruments."""

    def __init__(self) -> None:
        self._labels: list[str] = []
        self._instruments: dict[str, Instrument] = {}

        for instrument in [Dart(), Nims(), Zen()]:
            self._labels.append(instrument.label)
            self._instruments[instrument.label] = instrument

    def update_current_instrument(self, name: str) -> Instrument:
        """Update the current instrument based on the name.

        Args:
            name (str): Name of the instrument

        Returns
        -------
            Instrument: Instrument object
        """
        return self._instruments[name]

    @property
    def instrument_labels(self) -> list[str]:
        """Return the list of instrument labels.

        Returns
        -------
            list[str]: List of instrument labels
        """
        return self._labels
