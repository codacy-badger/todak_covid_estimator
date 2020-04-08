import json

data = '''
{
    "region": {
      "name": "Africa",
      "avgAge": 19.7,
      "avgDailyIncomeInUSD": 5,
      "avgDailyIncomePopulation": 0.71
    },
    "periodType": "days",
    "timeToElapse": 58,
    "reportedCases": 674,
    "population": 66622705,
    "totalHospitalBeds": 1380614
}
'''



def estimator(data):
  output = {}
  dataOuput= {}
  impact= {}
  severeImpact = {}
  json_data = json.loads(data)
  dataOuput.update(json_data)
  output.update({"data": dataOuput})
  reportedCases = json_data['reportedCases']
  timeToElapse = json_data['timeToElapse']
  totalHospitalBeds = json_data['totalHospitalBeds']
  avgDailyIncomeInUSD = json_data['region']['avgDailyIncomeInUSD']
  avgDailyIncomePopulation = json_data['region']['avgDailyIncomePopulation']

# IMPACT
  # CHALLENGE 1
  powerFactor = timeToElapse/3
  currentlyInfectedImpact = reportedCases * 10
  infectionsByRequestedTimeImpact = int(currentlyInfectedImpact * (2**powerFactor))
  # CHALLENGE 2
  severeCasesByRequestedTimeImpact = int(0.15 * infectionsByRequestedTimeImpact) 
  hospitalBedsByRequestedTimeImpact = int(totalHospitalBeds - severeCasesByRequestedTimeImpact)
  # CHALLENGE 3
  casesForICUByRequestedTimeImpact = int(0.05 * infectionsByRequestedTimeImpact) 
  casesForVentilatorsByRequestedTimeImpact = int(0.02 * infectionsByRequestedTimeImpact) 
  dollarsInFlightImpact = infectionsByRequestedTimeImpact *30* avgDailyIncomeInUSD * avgDailyIncomePopulation

  impact.update({"currentlyInfected": currentlyInfectedImpact})
  impact.update({"infectionsByRequestedTime": infectionsByRequestedTimeImpact})
  impact.update({"severeCasesByRequestedTime": severeCasesByRequestedTimeImpact})
  impact.update({"hospitalBedsByRequestedTime": hospitalBedsByRequestedTimeImpact})
  impact.update({"casesForICUByRequestedTime": casesForICUByRequestedTimeImpact})
  impact.update({"casesForVentilatorsByRequestedTime": casesForVentilatorsByRequestedTimeImpact})
  impact.update({"dollarsInFlight": dollarsInFlightImpact})

# SEVERELY IMPACT
  # CHALLENGE 1
  currentlyInfectedSevereImpact = reportedCases * 50
  infectionsByRequestedTimeSevereImpact = int(currentlyInfectedSevereImpact * (2**powerFactor))
  # CHALLENGE 2
  severeCasesByRequestedTimeSevereImpact = int(0.15 * infectionsByRequestedTimeSevereImpact)
  hospitalBedsByRequestedTimeSevereImpact = int(totalHospitalBeds - severeCasesByRequestedTimeSevereImpact)
  # CHALLENGE 3
  casesForICUByRequestedTimeSevereImpact = int(0.05 * infectionsByRequestedTimeSevereImpact) 
  casesForVentilatorsByRequestedTimeSevereImpact = int(0.02 * infectionsByRequestedTimeSevereImpact)
  dollarsInFlightSevereImpact = infectionsByRequestedTimeSevereImpact *30* avgDailyIncomeInUSD * avgDailyIncomePopulation

  severeImpact.update({"currentlyInfected": currentlyInfectedSevereImpact})
  severeImpact.update({"infectionsByRequestedTime": infectionsByRequestedTimeSevereImpact})
  severeImpact.update({"severeCasesByRequestedTime": severeCasesByRequestedTimeSevereImpact})
  severeImpact.update({"hospitalBedsByRequestedTime": hospitalBedsByRequestedTimeSevereImpact})
  severeImpact.update({"casesForICUByRequestedTime": casesForICUByRequestedTimeSevereImpact})
  severeImpact.update({"casesForVentilatorsByRequestedTime": casesForVentilatorsByRequestedTimeSevereImpact})
  severeImpact.update({"dollarsInFlight": dollarsInFlightSevereImpact})
 
# OUTPUT
  output.update({"impact": impact})
  output.update({"severeImpact": severeImpact})

  json_output = json.dumps(output)
  # print(json_output) 
  return json_output 

estimator(data)

