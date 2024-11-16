const track = document.querySelector('.carousel-track');
const slides = Array.from(track.children);
const nextButton = document.querySelector('#button-carrousel.next');
const prevButton = document.querySelector('#button-carrousel.prev');

// Obtener el ancho de una imagen
const slideWidth = slides[0].getBoundingClientRect().width;

// Colocar las imágenes una al lado de la otra (esto es crucial para el desplazamiento)
slides.forEach((slide, index) => {
    slide.style.left = slideWidth * index + 'px';
});

// Índice de la imagen actual
let currentIndex = 0;

// Función para mover el carrusel
const moveToSlide = (index) => {
    track.style.transform = `translateX(-${slideWidth * index}px)`;
};

// Navegar hacia adelante
nextButton.addEventListener('click', () => {
    if (currentIndex < slides.length - 1) {
        currentIndex++;
    } else {
        currentIndex = 0; // Volver al principio cuando llegamos al final
    }
    moveToSlide(currentIndex);
});

// Navegar hacia atrás
prevButton.addEventListener('click', () => {
    if (currentIndex > 0) {
        currentIndex--;
    } else {
        currentIndex = slides.length - 1; // Volver al final cuando llegamos al principio
    }
    moveToSlide(currentIndex);
});