function setNavBarSections() {
    const sections = document.querySelectorAll("h1, h2, h3");
    const navbar = document.querySelector(".navbar-nav");

    const toggler = document.getElementById("navbarToggler");
    const bsCollapse = new bootstrap.Collapse(toggler, { toggle: false });

    let index = 0;
    sections.forEach(function (section) {
        section.id = `section${index}`;
        index++;

        const entry = document.createElement("li");
        const entryLink = document.createElement("a");

        entry.appendChild(entryLink);
        navbar.appendChild(entry);

        entry.classList.add("nav-item");
        entryLink.classList.add("nav-link", "btn", "btn-light", "text-start", "ps-2");

        entryLink.href = `#${section.id}`;
        entryLink.textContent = section.hasAttribute("data-toc")
            ? section.dataset.toc
            : section.textContent;

        entryLink.addEventListener("click", () => { bsCollapse.toggle() });
    });
};

document.addEventListener("DOMContentLoaded", setNavBarSections());
