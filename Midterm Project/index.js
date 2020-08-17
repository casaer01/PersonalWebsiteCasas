// https://github.com/toddmotto/public-apis#weather

// https://developer.valvesoftware.com/wiki/Steam_Web_API#GetNewsForApp_.28v0002.29
// http://steamwebapi.azurewebsites.net/

// Steam web API Key: BE68484C46B850AACC83630F2EF9C8A3
// Domain Name: localhost

//https://www.metaweather.com/api/ - Metaweather api
//http://woeid.rosselliot.co.nz/lookup/decorah WOEID look up
//WOEID: 2390252
//most likely will use Dark sky api for the weather

//Dark sky api key: 8aabe5bc9852b4337151174b713dd42a

async function getData(url) {
    var valreturn = fetch(url)
        .then(response => response.json())
        .catch(error => console.log(error));
        return valreturn
}

async function warframeapi() {
    var warframeWeb = document.querySelector('#warframeWeb')
    // var warframeAlerts = document.querySelector('#warframeAlerts')
    warframeWeb.innerHTML = '<h2 class="card-header"> Warframe News <button type="button" class="btn btn-success" onclick="warframeapi()">Refresh</button></h2>'

    let warframeData = await Promise.all([getData('https://api.warframestat.us/pc')])

    //console.log(warframeData[0])
    warframeNews = warframeData[0]['news']
    // warframeAlert = warframeData[0]['alerts']

    for (let i in warframeNews) {
        let postDiv = document.createElement('div')

        let postHead = document.createElement('div')
        //postHead.classList.add('row')

        let PostTitleDiv = document.createElement('h2')
        PostTitleDiv.classList.add('alert', 'alert-dark')
        PostTitleDiv.setAttribute('href', warframeNews[i]['link'])
        PostTitleDiv.innerHTML = 
            '[' + warframeNews[i]['eta'] + '] ' + 
            '<a href=' + warframeNews[i]['link'] + '>' + warframeNews[i]['message'] + '</a>'
        postHead.appendChild(PostTitleDiv)

        postDiv.appendChild(postHead)

        warframeWeb.appendChild(postDiv)
        console.log('warframe appendChild')
    }

    // for (let i in warframeAlert) {
    //     let postDiv = document.createElement('div')

    //     let postHead = document.createElement('div')
    //     //postHead.classList.add('row')

    //     let PostTitleDiv = document.createElement('h2')
    //     PostTitleDiv.classList.add('alert', 'alert-dark')
    //     //PostTitleDiv.setAttribute('href', warframeNews[i]['link'])
    //     PostTitleDiv.innerHTML = 'Location: ' + warframeAlert[i]['mission']['node'] +  '   Timer: ' + warframeAlert[i]['eta'] + ' left'
    //     postHead.appendChild(PostTitleDiv)

    //     let postBody = document.createElement('h3')
    //     postBody.classList.add('alert', 'alert-info')
    //     postBody.innerHTML = 
    //         '<p> Mission Type: ' + warframeAlert[i]['mission']['type'] + '</p>' +
    //         '<p> Enemy Levels: ' + warframeAlert[i]['mission']['minEnemyLevel'] + ' - ' + warframeAlert[i]['mission']['maxEnemyLevel'] + '</p>' +
    //         '<p> Rewards: ' + warframeAlert[i]['mission']['reward']['itemString'] + ' ' + warframeAlert[i]['mission']['reward']['credits'] + ' credits' + '</p>'
    //     postHead.appendChild(postBody)

    //     postDiv.appendChild(postHead)

    //     warframeAlerts.appendChild(postDiv)
    // }
}

async function warframealertsapi() {
    var warframeAlerts = document.querySelector('#warframeAlerts')

    warframeAlerts.innerHTML = '<h2 class="card-header"> Warframe Alerts <button type="button" class="btn btn-success" onclick="warframealertsapi()" >Refresh</button></h2>'

    let warframeData = await Promise.all([getData('https://api.warframestat.us/pc')])

    warframeAlert = warframeData[0]['alerts']

    for (let i in warframeAlert) {
        let postDiv = document.createElement('div')

        let postHead = document.createElement('div')
        //postHead.classList.add('row')

        let PostTitleDiv = document.createElement('h2')
        PostTitleDiv.classList.add('alert', 'alert-dark')
        //PostTitleDiv.setAttribute('href', warframeNews[i]['link'])
        PostTitleDiv.innerHTML = 'Location: ' + warframeAlert[i]['mission']['node'] +  '   Timer: ' + warframeAlert[i]['eta'] + ' left'
        postHead.appendChild(PostTitleDiv)

        let postBody = document.createElement('h3')
        postBody.classList.add('alert', 'alert-info')
        postBody.innerHTML = 
            '<p> Mission Type: ' + warframeAlert[i]['mission']['type'] + '</p>' +
            '<p> Enemy Levels: ' + warframeAlert[i]['mission']['minEnemyLevel'] + ' - ' + warframeAlert[i]['mission']['maxEnemyLevel'] + '</p>' +
            '<p> Rewards: ' + warframeAlert[i]['mission']['reward']['itemString'] + ' ' + warframeAlert[i]['mission']['reward']['credits'] + ' credits' + '</p>'
        postHead.appendChild(postBody)

        postDiv.appendChild(postHead)

        warframeAlerts.appendChild(postDiv)
    }

}


async function steamPopulate() {
    
    var steamweb = document.querySelector('#steamWeb')
    
    var numLength = document.querySelector('#numLength').value

    steamweb.innerHTML = '<h2 class="card-header"> Steam News <input type="number" id="numLength" size="3" value="' + numLength + '"/><button type="button" class="btn btn-success" onclick="steamPopulate()">Refresh</button> </h2><p></p>'

    //let news = await Promise.all([getData('http://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?key=BE68484C46B850AACC83630F2EF9C8A3&appid=230410&count=5&maxlength=300&format=json')])

    let news = await Promise.all([getData('http://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?key=BE68484C46B850AACC83630F2EF9C8A3&appid=230410&count='+ numLength +'&maxlength=300&format=json')])

    
    //console.log(news[0]['appnews']['newsitems'])
    let steamapi = news[0]['appnews']['newsitems']
    
    for (let i in steamapi) {
        let postDiv = document.createElement('div')

        let postHead = document.createElement('div')
        //postHead.classList.add('row')

        let PostTitleDiv = document.createElement('h3')
        PostTitleDiv.classList.add()
        PostTitleDiv.innerHTML = steamapi[i]['title']
        postHead.appendChild(PostTitleDiv)

        let userInfo =  document.createElement('div')
        userInfo.classList.add('alert','alert-info')
        userInfo.innerHTML = steamapi[i]['contents'] + '<a href='+ steamapi[i]['url'] + '>' + ' Click here to read more' + '</a>'
        postHead.appendChild(userInfo)
        //console.log('passed description')

        postDiv.appendChild(postHead)

        steamweb.appendChild(postDiv)
    }
}

// async function weatherPopulate() {

//     //let weather = await Promise.all([getData('api/location/2390252/')])
//     //let weather = await Promise.all([getData('https://www.metaweather.com/api/location/search/?query=san')])
//     let weather = await Promise.all([getData('https://api.darksky.net/forecast/8aabe5bc9852b4337151174b713dd42a/43.303291,-91.788338')])

//     console.log(weather)
// }
$(document).ready(function () {
    warframeapi()
    warframealertsapi()
    steamPopulate()
});