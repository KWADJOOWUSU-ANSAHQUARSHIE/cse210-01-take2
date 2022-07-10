const dataURL = 'json/pests.json';
const listDiv = document.querySelector('.list-view');
const cardDiv = document.querySelector('.grid-view');

// fetching of data from github.com

fetch(dataURL)
    .then((response) => {
        return response.json();
    })
    .then((jsonObject) => {
        console.table(jsonObject);

        const pests = jsonObject['pests'];
        pests.forEach(displaypestsInGrid);
        pests.forEach(displaypestsInList);
    });

function displaypestsInList(pests) {

    let media_card = document.createElement('section');
    let h2 = document.createElement('h2');
    let phone = document.createElement('p');

    h2.textContent = pests.name
    phone.textContent = pests.phone
    
    media_card.appendChild(h2);
    media_card.appendChild(phone);

    listDiv.appendChild(media_card);
}

function displaypestsInGrid(pests) {

    let h2 = document.createElement('h2');
    let image = document.createElement('img');
    let hr = document.createElement('hr');
    let phone = document.createElement('p');
    let media_card = document.createElement('section');
  
    media_card.appendChild(hr);
    media_card.appendChild(phone);
    media_card.appendChild(image);
    media_card.appendChild(h2);

    cardDiv.appendChild(media_card);
    
    h2.textContent = `${pests.name}`
    phone.textContent = `${pests.phone}`

    image.setAttribute("src", pests.imageurl);
    image.setAttribute("alt", `Logo of ${pests.name}`);
    image.setAttribute("loading", "lazy");
}

