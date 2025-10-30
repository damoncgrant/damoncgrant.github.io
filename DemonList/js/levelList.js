async function getLevels() {
    const res = await fetch("levels.json");
    const levels = await res.json();

    return levels;
}

async function displayLevels() {
    const levels = await getLevels();
    const container = document.getElementById("levelContainer");

    var current = 1;

    levels.levels.forEach(level => {
        // Create the level card
        const levelCard = document.createElement("div");
        levelCard.classList.add("levelCard");
        
        const mainInfo = document.createElement("div");
        mainInfo.classList.add("mainInfo")
        mainInfo.innerHTML = `
        <h3>#${current.toString()} - ${level.name}</h3>
        <h4>published by ${level.creator}</h4>
        `
        
        // Creating the thumbnail which is clickable
        const thumbnailLink = document.createElement("a");
        thumbnailLink.href=level.videoLink;
        thumbnailLink.target="__blank"
        const thumbnail = document.createElement("img");
        thumbnail.src = `images/thumbnails/${level.name}.jpg`;
        thumbnail.width = 246
        thumbnail.height = 144
        thumbnailLink.appendChild(thumbnail)
        thumbnailLink.classList.add("thumbnail")
        mainInfo.appendChild(thumbnailLink);

        // Create the more details
        const details = document.createElement("div");
        details.classList.add("details");
        details.innerHTML = `
            <p class="date">Completed on <b>${level.completionDate}</b></p>
            <p class="attempts">Attempt Count: <b>${level.attempts.toString()}</b></p>
            <p class="enjoyment">Enjoyment: <b>${level.enjoyment}</b></p>
            <p class="worstFail">Worst Fail: <b>${level.worstFail}%</b></p>
        `

        levelCard.addEventListener("click", event => {

            if (event.target.closest("a")) return;

            levelCard.classList.toggle("open")
        })

        levelCard.appendChild(mainInfo);
        levelCard.appendChild(details);
        container.appendChild(levelCard);
        current += 1;
    })

}

displayLevels();

