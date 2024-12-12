//Episodios Temporada 1

const episodes = {
    1: {
        title: "Episodio 1: 'Hola Mundo!'",
        description: "Mauricio, cansado de la monotonía como técnico informático, decide dar un vuelco a su vida. Siguiendo las últimas tendencias se da cuenta de que el futuro está en la Inteligencia Artificial, así que inicia un duro camino de aprendizaje para destacar en ese nuevo mundo desconocido para él.",
        link: "https://github.com/tu-usuario/episodio-01" 

    },
    2:{
        title: "Episodio 2: La calculadora",
        description: "Tras unas nociones básicas de programación, Mauricio empieza a desarrollar una calculadora.",
        link: "https://github.com/tu-usuario/episodio-02"
    },
    3:{
        title: "Episodio 3: Lo siguiente",
        description: "Tras unas nociones básicas de programación, Mauricio empieza a desarrollar una calculadora.",
        link: "https://github.com/tu-usuario/episodio-03"
    },
};

// Mostrar el contenido de un episodio

function showEpisode(episodeNumber) {
    const episode = episodes[episodeNumber];
    const detailsContainer = document.getElementById("episode-details");

    if (episode) {
        detailsContainer.innerHTML =
            <h3>${episode.title}</h3>,
            <p>${episode.description}</p>,
            <a href="$(episode.link)" target="_blank">Ver proyecto en GitHub</a>
         ;
        
         // Marca la pestaña activa
        const tabs = document.querySelectorAll(".tab");
        tabs.forEach(tab =>tab.classList.remove("active"));
        tabs[episodeNumber - 1].classList.add("active"); 
    }
}

// Leer el parámetro de la URL

function getEpisodeFromUrl(){
    const params = new URLSearchParams(window.location.search);
    return params.get("episodio");
}

//Inicializar la página

document.addEventListener("DOMContentLoaded", () => {
    const initialEpisode = getEpisodeFromUrl() || 1;
    showEpisode(Number(initialEpisode));
});