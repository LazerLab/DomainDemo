# Introduction

This directory contains the classification labels for domains we collected from existing datasets.
These labels are used for validating our derived metrics.

# Localness

`news_local_national_classification.csv` contains the local and national classification for news domains.

These labels are collected from the following sources:

| Dataset | Link |
| --- | --- |
|Cronin et al.| https://github.com/ercexpo/us-news-domains |
|Fisher et al.| https://osf.io/hwuxf/?view_only=3fa7499661df487689031e11b8ea20b4 |
|Yin et al.| https://github.com/yinleon/LocalNewsDataset |
|Horne et al.| https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/GFE66K |
|ABYZ | http://www.abyznewslinks.com/unite.htm |

Please refer to the paper for how we merge and clean the labels.

# Partisan Bias

`partisan_bias_scores.csv` contains the partisan bias scores for news domains.
Here are the sources of the labels:

| Column Name | Dataset | Link |
| --- | --- | --- |
| fb_score | Bakshy et al. | https://doi.org/10.7910/DVN/QAN5VX |
| mturk_score | Robertson et al. | https://doi.org/10.7910/DVN/QAN5VX |
| allsides_score | AllSides | https://doi.org/10.7910/DVN/QAN5VX |
| allsides_score_community | AllSides community | https://doi.org/10.7910/DVN/QAN5VX |
| mbfc_score | MBFC (Media Bias Fact Check) | https://mediabiasfactcheck.com  |
| media_score | Eady et al. | https://gregoryeady.com |
| buntain_share_ideology_score | Buntain et al. | https://osf.io/wtf9y |
