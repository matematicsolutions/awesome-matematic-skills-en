# Firm deployment standard

Shared standard for every skill in this repo. Before production material goes into use, the firm makes these decisions. They cover data, contracts and the audit trail.

## Decisions before first use

- **Data map** - which categories of data enter the tool at all, and which stay out (privileged, particularly sensitive).
- **Processor agreement (GDPR Art. 28)** - with every provider that processes personal data. Check retention, sub-processing and transfers outside the EEA.
- **Anonymisation on input** - set when personal data is replaced with placeholders locally, before anything leaves for the API.
- **Confidentiality threshold** - the rule for when material is not brought into the tool at all. Default: when in doubt, do not transfer.

## Audit trail

Every high-stakes output leaves a trace: model, date, sources, confidence class, who approved it. This is evidence of due diligence under the AI Act (Art. 12, record-keeping), not bureaucracy - it matters when someone asks what a decision was based on.

## Roles

- The lawyer carries professional responsibility for the output and is the gate before anything goes out.
- The tool prepares a draft and a reasoning trace.
- The data controller is responsible for processor agreements and the data map.

## What this standard does NOT do

- It does not replace a data protection impact assessment (DPIA) where one is required.
- It does not negotiate the processor agreement for the firm - it only flags that one is needed.
- It does not decide whether a given provider meets the requirements - that is the firm's assessment.
