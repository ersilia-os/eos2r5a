# Retrosynthetic accessibility score

Retrosynthetic accessibility score based on the computer aided synthesis planning tool AiZynthfinder. The authors have selected a ChEMBL subset of 200.000 molecules, and checked whether AiZinthFinder could identify a synthetic route or not. This data has been trained to create a classifier that computes 4500 times faster than the underlying AiZynthFinder. Molecules outside the applicability domain, such as the GBD database, need to be fine tuned to their use case.

## Identifiers

* EOS model ID: `eos2r5a`
* Slug: `retrosynthetic-accessibility`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Regression`
* Output: `Score`
* Output Type: `Float`
* Output Shape: `Single`
* Interpretation: Higher score indicates easier retrosynthetic accessibility

## References

* [Publication](https://pubs.rsc.org/en/content/articlelanding/2021/sc/d0sc05401a)
* [Source Code](https://github.com/reymond-group/RAscore)
* Ersilia contributor: [miquelduranfrigola](https://github.com/miquelduranfrigola)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos2r5a)

## Citation

If you use this model, please cite the [original authors](https://pubs.rsc.org/en/content/articlelanding/2021/sc/d0sc05401a) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a MIT license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!