console.log('HI')

const data = fetch(`https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${key}`).then(res => res.json()).then(data => console.log(data))