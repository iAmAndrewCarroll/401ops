# Lab 1: Cyber Risk Analysis

## Overview
Cybersecurity risk analysis is vital in your efforts to identify, protect, and manage all your client’s information data, systems, and resources. Risk analysis allows you to ultimately create a suitable plan to secure and manage risks for the organization.

## Scenario
A third party has recently performed a cyber hygiene assessment for Initrobe. The CTO has requested you compose a risk assessment report as part of the company’s strategic planning efforts.

The CTO also asked you “What if the cloud data center gets flooded? We’ve heard that the proposed region we’ll be using is located in a physical area susceptible to floods.”

The data center is valued at 6,173,160.00 USD. If a flooding happens 15-30% of the data center is estimated to be compromised. The flooding tends to happen every four to six years.

## Objectives
- Create a risk assessment report for Initrobe.
- Perform a quantitative deterministic risk analysis against the data center scenario.

## Resources
- CyHy Sample Report_508C.pdf
- Risk Assessment Worksheet.xlsx
- Deterministic Risk Analysis (disregard the product marketing…)

## Tasks
### Part 1: Review the CyHy Report
- Read through the CyHy Report and identify potential risks
- Take notes as needed

### Part 2: Create the Risk Assessment Report
- Using the provided Excel worksheet, populate the fields and submit the completed worksheet.
- What are the biggest cyber risks to Initrobe?
- Justify your reasoning.
- For each risk, what are at least two ways we could mitigate the risk?
- For each risk, what is the most effective risk mitigation technique of the ideas you came up with? This should be the lowest cost and greatest mitigation.

[Risk Assessment Worksheet](./Risk%20Assessment%20Worksheet.xlsx)

### Part 3: Quantitative Deterministic Risk Calculation
### Worst Case Scenario
- **Exposure Factor (EF)**: 30%. Justification: Represents the highest potential damage in case of flooding.
- **Annual Rate of Occurrence (ARO)**: 1/5 (once every 5 years). Justification: Average interval between floods (4 to 6 years).
- **Single Loss Expectancy (SLE)**: $1,851,948.00. Calculation: AV * EF.
- **Annual Loss Expectancy (ALE)**: $370,389.60. Calculation: SLE * ARO.

### Best Case Scenario
- **EF**: 15%. Justification: Assumes minimal impact from flooding.
- **ARO**: 1/6 (once every 6 years). Justification: Considering a less frequent occurrence of flooding.
- **SLE**: $925,974.00. Calculation: AV * EF.
- **ALE**: $154,329.00. Calculation: SLE * ARO.

### Most Likely Scenario
- **EF**: 22.5% (average of worst and best cases). Justification: A balanced estimate between the extremes.
- **ARO**: 1/5 (once every 5 years). Justification: Same as worst case, a reasonable average.
- **SLE**: $1,388,961.00. Calculation: AV * EF.
- **ALE**: $277,792.20. Calculation: SLE * ARO.

- Create a table in your Google Doc submission of the calculated values for all three scenarios. Convert and present the monetary figures in USD for all fields of the table, and include the conversion rate used.

| Scenario         | Exposure Factor (EF) | Annual Rate of Occurrence (ARO) | Single Loss Expectancy (SLE) | Annual Loss Expectancy (ALE) |
|------------------|----------------------|---------------------------------|------------------------------|------------------------------|
| Worst Case       | 30%                  | 1/5 (once every 5 years)         | $1,851,948.00 USD            | $370,389.60 USD              |
| Best Case        | 15%                  | 1/6 (once every 6 years)         | $925,974.00 USD              | $154,329.00 USD              |
| Most Likely Case | 22.5%                | 1/5 (once every 5 years)         | $1,388,961.00 USD            | $277,792.20 USD              |
