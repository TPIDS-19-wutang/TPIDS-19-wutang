let acordion = document.getElementsByClassName("acordion");
let i

for (i = 0; i < acordion.length; i++) {
    acordion[i].addEventListener("click", function () {
        this.classList.toggle("active_acordion");

        let panel = this.nextElementSibling;
        if (panel.style.display === 'block') {
            panel.style.display = 'none';
        }
        else {
            panel.style.display = 'block';
        }
    })
}