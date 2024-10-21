function validateForm() {
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const message = document.getElementById("message").value;

    if (!name || !email || !message) {
        alert("Будь ласка, заповніть всі поля!");
        return false;
    }

    alert("Дякуємо за ваше повідомлення, " + name + "!");
    return true;
}
