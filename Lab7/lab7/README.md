# Lab 7 - Fuzz Testing for Input Validation Bugs

This folder contains the completed Lab 7 submission for the vending machine application.

## Files
- `vending_machine.py` - corrected application with defensive input validation.
- `test_vending_machine.py` - Hypothesis fuzz tests, valid-input tests, and invalid-input validation tests.
- `Lab7_FuzzTesting_Submission_Report.pdf` - experiment report with the title page and execution evidence.
- `screenshots/` - four terminal screenshots in execution order.

## Run locally
From this folder, install dependencies and run the application/tests:

```powershell
python -m pip install hypothesis pytest
python vending_machine.py
python -m pytest test_vending_machine.py -v
```

The recorded final test run collected 21 tests and passed all 21.
