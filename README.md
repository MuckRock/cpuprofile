# CPU Profile

This is a simple package to measure CPU speed by calculating the time it takes to
compute Fibonacci numbers. It is useful in contexts where CPU speed is unknown or can
fluctuate, such as cloud function environments, and can serve as a rough measure of how
long subsequent compute-intensive code will take to run.

## Installation

```sh
pip install cpuprofile
```

## Usage

```python
from cpuprofile import profile_cpu

# Calculate the CPU speed by computing Fibonacci numbers.

elapsed_time = profile_cpu()

# elapsed_time is ~0.18 (seconds) on a 2.5 GHz Intel Core i7 2015 Macbook Pro.

# Or, a number can be specified to calculate the nth Fibonacci (default: 28).

elapsed_time = profile_cpu(15)  # 15th Fibonacci; takes around 0.0006 seconds
elapsed_time = profile_cpu(35)  # 35th Fibonacci; takes about 5 seconds
```

## Credit

The minimalist approach of recursively calculating Fibonacci numbers as a way to profile
the CPU is inspired by:

- Booth, J. (2015).
  [Not so incognito: Exploiting resource-based side channels in javascript engines](http://jombooth.com/static/thesis.pdf)
  (Undergraduate thesis, Harvard University).
