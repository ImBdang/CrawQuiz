questions = document.getElementById("questions")
dulieu = null

async function getDulieu(){
    dulieu = await fetch("../../data/Questions.txt")
        .then(res=> res.json())
}

async function getToken(){
    token = await fetch("../../data/token.txt")
    .then(res=>res.text())
    return token
}



function run(){
    index = 1
    dulieu = dulieu["data"][0]["test"]
    p = ""
    for (const i of dulieu){
        p1 = ""
        p2 = ""
        ans = i.answer_option

        for (const j of ans){
            p1 += `<label class="answer-option">
                        <div class="cautraloi">
                            <input type="${i.question_type}" name="question-${index}" value=${index}>
                            ${j.value}
                        </div>
                    </label><br>`
        }


        p2 =`
        <div class="question">
            <div class="cauhoi">
                ${index}. ${i.question_direction} (Kieu cau hoi: ${i.question_type})
            </div><br>
        <div class="answer-options">`
        p2 += p1
        p2 +=`
            </div>
        </div>`
        p+=p2
        index++
    }
    questions.innerHTML = p
}


async function getImage(url, token) {
    const response = await fetch(url, {
        method: 'GET',
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Accept-Language': 'en-US,en;q=0.9',
            'Authorization': token,
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Host': 'apps.ictu.edu.vn:9087',
            'Origin': 'https://lms.ictu.edu.vn',
            'Referer': 'https://lms.ictu.edu.vn/',
            'Sec-CH-UA': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
            'Sec-CH-UA-Mobile': '?0',
            'Sec-CH-UA-Platform': '"Linux"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
            'X-App-Id': '7040BD38-0D02-4CBE-8B0E-F4115C348003'
        }
    });
    const blob = await response.blob();
    const imgUrl = URL.createObjectURL(blob);
    return imgUrl;
}

async function changeImageSources() {
    const images = document.querySelectorAll('img[data-org="serverAws"]');
    for (const img of images) {
        const imgSrc = img.getAttribute('src');
        const token = await getToken()
        const url = `https://apps.ictu.edu.vn:9087/ionline/api/aws/file/${imgSrc}?token=${token}`
        const newSrc = await getImage(url, token);
        img.src = newSrc;
    }
}

function saveAsPDF() {
    window.print(); 
}


async function main(){
    await getDulieu()
    await run()
    await changeImageSources()
}

main()

