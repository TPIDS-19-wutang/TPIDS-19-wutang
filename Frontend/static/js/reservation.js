document.getElementById("id_hotel").addEventListener("change", function () {
    var selectedOption = this.options[this.selectedIndex];
var hotelLocation = selectedOption.getAttribute("data-location");
document.getElementById("hotel_location").value = hotelLocation;
});