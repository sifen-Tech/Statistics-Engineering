\# Statistical Engine \& Monte Carlo Simulation



\## Project Overview

This project implements a pure-Python statistical engine (`StatEngine`) to compute mean, median, mode, variance, standard deviation, and detect outliers.  

It also includes a Monte Carlo simulation to model a startup server's daily crash probability, demonstrating the Law of Large Numbers (LLN).



\## Mathematical Logic

\- \*\*Mean:\*\* Sum of all numbers divided by count.  

\- \*\*Median:\*\* Middle value after sorting (average of two middle values if even).  

\- \*\*Mode:\*\* Most frequent values; handles multimodal and unique data.  

\- \*\*Variance:\*\* Measures data spread. Supports:

&#x20; - \*\*Population variance:\*\* Divide squared differences by N.  

&#x20; - \*\*Sample variance:\*\* Divide squared differences by N-1 (Bessel’s correction).  

\- \*\*Standard deviation:\*\* Square root of variance.  

\- \*\*Outliers:\*\* Data points more than `threshold` standard deviations from mean.





