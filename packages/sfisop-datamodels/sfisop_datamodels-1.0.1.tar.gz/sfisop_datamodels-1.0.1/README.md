# SmartOcean timeseries data model

The purpose of the data model is to support the exchange of time series data in particular exchange of fragments of data 
associated with time series delivered by the SFI Smart Ocean Platform: https://smartoceanplatform.github.io/ 

The data model is implemented based on the Pydantic framework: https://docs.pydantic.dev/latest/

# Standards

The `parameter` and `unit` in the `Observation` class is to follow the Copernicus Marine in-situ TAC physical parameters list:

https://archimer.ifremer.fr/doc/00422/53381/

The `qualityCodes` is to follow the recommendations for in-situ data Near Real Time Quality Control:

https://archimer.ifremer.fr/doc/00251/36230/


The `time` object variable in the `Datapoint` class is to follow the ISO8601 standard and include timezone information.

# Example of use

The code below provides an example of ow to use the classes of the library.

```python
from sfisop.datamodels.tsdatamodel.timeseriesdata import *

a_location = Location(latitude=5.0, longitude=65)

meta_data = MetaData(description="test time series",
                     timeseries="timeseries_testdata",
                     origin="timeseries_testdata")

observation = Observation(source="test sensor",
                          source_id="test sensor id",
                          parameter="temperature",
                          value="5.0",
                          unit="celcius",
                          qualityCodes=[0])

data_point = DataPoint(dp_id="datapoint id",
                       source="test sensor hub",
                       source_id="test sensor hub id",
                       location=a_location,
                       time="2024-02-17T20:12:49.559547+01:00",
                       observations=[observation])

data_points = [data_point]

ts_data = TimeSeriesData(format="SMARTOCEAN_V1",
                         metadata=meta_data,
                         data=data_points)
```

The utility functions implemented in the `tsdata_utils.py` and `timeseriesdata.py` is to be used for serialisation and de-serialisation of time series data.

Further documentation can be found on the SFI Smart Ocean platform web pages: https://smartoceanplatform.github.io/interoperability/

