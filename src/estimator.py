import json

data = {
  'region': {
      'name': "Africa",
      'avgAge': 19.7,
      'avgDailyIncomeInUSD': 5,
      'avgDailyIncomePopulation': 0.71
    },
    'periodType': "days",
    'timeToElapse': 58,
    'reportedCases': 674,
    'population': 66622705,
    'totalHospitalBeds': 1380614
}
      



def estimator(**data):
  output = {}
  dataOuput= {}
  impact= {}
  severeImpact = {}
  output.update({"data": data})
  reportedCases = data['reportedCases']
  periodType = data['periodType']
  timeToElapse = data['timeToElapse']
  totalHospitalBeds = data['totalHospitalBeds']
  avgDailyIncomeInUSD = data['region']['avgDailyIncomeInUSD']
  avgDailyIncomePopulation = data['region']['avgDailyIncomePopulation']

# IMPACT
  # CHALLENGE 1
  currentlyInfectedImpact = reportedCases * 10
  if periodType == "days" :
    powerFactor = timeToElapse/3
    infectionsByRequestedTimeImpact = int(currentlyInfectedImpact * (2**powerFactor))
  if periodType == "weeks" :
    powerFactor = (timeToElapse*7)/3
    infectionsByRequestedTimeImpact = int(currentlyInfectedImpact * (2**powerFactor))
  if periodType == "months" :
    powerFactor = (timeToElapse*30)/3
    infectionsByRequestedTimeImpact = int(currentlyInfectedImpact * (2**powerFactor))
  # CHALLENGE 2
  severeCasesByRequestedTimeImpact = int(0.15 * infectionsByRequestedTimeImpact) 
  hospitalBedsByRequestedTimeImpact = int(totalHospitalBeds - severeCasesByRequestedTimeImpact)
  # CHALLENGE 3
  casesForICUByRequestedTimeImpact = int(0.05 * infectionsByRequestedTimeImpact) 
  casesForVentilatorsByRequestedTimeImpact = int(0.02 * infectionsByRequestedTimeImpact) 
  dollarsInFlightImpact = round((infectionsByRequestedTimeImpact *30* avgDailyIncomeInUSD * avgDailyIncomePopulation),2)

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
  if periodType == "days" :
    powerFactor = timeToElapse/3
    infectionsByRequestedTimeSevereImpact = int(currentlyInfectedSevereImpact * (2**powerFactor))
  if periodType == "weeks" :
    powerFactor = (timeToElapse*7)/3
    infectionsByRequestedTimeSevereImpact = int(currentlyInfectedSevereImpact * (2**powerFactor))
  if periodType == "months" :
    powerFactor = (timeToElapse*30)/3
    infectionsByRequestedTimeSevereImpact = int(currentlyInfectedSevereImpact * (2**powerFactor))
  # CHALLENGE 2
  severeCasesByRequestedTimeSevereImpact = int(0.15 * infectionsByRequestedTimeSevereImpact)
  hospitalBedsByRequestedTimeSevereImpact = int(totalHospitalBeds - severeCasesByRequestedTimeSevereImpact)
  # CHALLENGE 3
  casesForICUByRequestedTimeSevereImpact = int(0.05 * infectionsByRequestedTimeSevereImpact) 
  casesForVentilatorsByRequestedTimeSevereImpact = int(0.02 * infectionsByRequestedTimeSevereImpact)
  dollarsInFlightSevereImpact = round((infectionsByRequestedTimeSevereImpact *30* avgDailyIncomeInUSD * avgDailyIncomePopulation),2)

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

  # json_output = json.dumps(output)
  # print(json_output) 
  # print(output) 
  # return json_output 
  return output



