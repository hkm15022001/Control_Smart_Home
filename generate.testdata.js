const fs = require('fs');

// read from json file
const rawData = fs.readFileSync('data.json');
const data = JSON.parse(rawData);
//generate test data
const getRandomPatterns = (data, numberOfPatterns) => {
  const dataIntents = data.intents;

  const testIntent = dataIntents.map((dataIntent, index) => {
    const patternCount = dataIntent.patterns.length;
    const testPatterns = []
    let i = 0
    while (i < 10) {
      const randomPattern = dataIntent.patterns[Math.floor(Math.random() * patternCount)];
      if (!testPatterns.includes(randomPattern)) {
        testPatterns.push(randomPattern);
        ++i;
      }
    }
    return {
      tag: dataIntent.tag,
      patterns: testPatterns
    }
  });
  return testIntent;
}
//substract file
const subData = (data, subData) => {
  const dataIntents = data.intents;
  const subDataIntents = subData.intents;
  dataIntents.forEach((dataIntent) => {
    subDataIntents.forEach((subDataIntent) => {
      if (dataIntent.tag === subDataIntent.tag) {
        dataIntent.patterns = dataIntent.patterns.filter((ele) => !subDataIntent.patterns.includes(ele))
        // console.log("trong vong lap",dataIntents)
      }
    })
  })
  return dataIntents
}
//save to file
const saveJsonFlie = (fileName,jsonString) => {
  fs.writeFile(fileName, jsonString, 'utf8', (err) => {
    if (err) {
      console.error('Error writing to file:', err);
    } else {
      console.log('JSON object has been saved to ',fileName);
    }
  });
}
// number of test you want
const numberOfTestPatterns = 10;
const testIntents = getRandomPatterns(data, numberOfTestPatterns);
const testData = {
  intents: testIntents
}
//get data file after substract test file
const trainIntents = subData(data, testData)
const dataTrain = {
  intents: trainIntents
}
const testJson = JSON.stringify(testData);
const trainJson = JSON.stringify(dataTrain);

saveJsonFlie("test.json",testJson);
saveJsonFlie("train.json",trainJson);

