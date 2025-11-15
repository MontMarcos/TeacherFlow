    function openSettings() {
        document.getElementById("settings-overlay").classList.remove("hidden");
    }
    function closeSettings() {
        document.getElementById("settings-overlay").classList.add("hidden");
    }
    document.getElementById("settings-overlay").addEventListener("click", function(e) {
        if (e.target === this) closeSettings();
    });
