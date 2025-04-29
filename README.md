# Retrosynthetic accessibility score

Retrosynthetic accessibility score based on the computer aided synthesis planning tool AiZynthfinder. The authors have selected a ChEMBL subset of 200.000 molecules, and checked whether AiZinthFinder could identify a synthetic route or not. This data has been trained to create a classifier that computes 4500 times faster than the underlying AiZynthFinder. Molecules outside the applicability domain, such as the GBD database, need to be fine tuned to their use case.

This model was incorporated on 2021-10-19.

## Information
### Identifiers
- **Ersilia Identifier:** `eos2r5a`
- **Slug:** `retrosynthetic-accessibility`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Property calculation or prediction`
- **Biomedical Area:** `Any`
- **Target Organism:** `Not Applicable`
- **Tags:** `Synthetic accessibility`, `Chemical synthesis`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** Higher score indicates easier retrosynthetic accessibility

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| ra_score | float | high | Retrosynthetic accessibility score |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos2r5a](https://hub.docker.com/r/ersiliaos/eos2r5a)
- **Docker Architecture:** `AMD64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos2r5a.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos2r5a.zip)

### Resource Consumption
- **Model Size (Mb):** `47`
- **Environment Size (Mb):** `1146`
- **Image Size (Mb):** `1212.51`

**Computational Performance (seconds):**
- 4 inputs: `30.43`
- 20 inputs: `20.21`
- 100 inputs: `20.37`

### References
- **Source Code**: [https://github.com/reymond-group/RAscore](https://github.com/reymond-group/RAscore)
- **Publication**: [https://pubs.rsc.org/en/content/articlelanding/2021/sc/d0sc05401a](https://pubs.rsc.org/en/content/articlelanding/2021/sc/d0sc05401a)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2021`
- **Ersilia Contributor:** [miquelduranfrigola](https://github.com/miquelduranfrigola)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [MIT](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos2r5a
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos2r5a
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
