# Storage management

The scraped data is recorded to the external drive using MySQL backups and tablespaces.
The external drive has been chosen as a budget solution to store large amount of data.

## Data workflow

Scraped records are sent directly to the localhost MySQL database instance through Scrapy Pipelines.
The MySQL database instance is hosted on a local Docker container that consists two volumes:
- Data mount - mount path to the external drive to store tablespaces and backups
- MySQL volume - contains mysql system schema to instantiate the same mysql setting accross different environments

The data then can be extracted based on MySQL features and user's preferences.

## Appendix

### Data sample

```SQL```
