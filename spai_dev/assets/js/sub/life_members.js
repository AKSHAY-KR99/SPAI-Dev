document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('.menu-icon').addEventListener('click', function () {
        document.querySelector('.navbar').classList.toggle('active');
    });
});
document.querySelectorAll('.tab-item').forEach(item => {
    item.addEventListener('click', function () {
        // Remove active class from all tabs
        document.querySelectorAll('.tab-item').forEach(tab => tab.classList.remove('active'));
        // Add active class to the clicked tab
        this.classList.add('active');

        // Hide all tab panels
        document.querySelectorAll('.table').forEach(panel => panel.classList.remove('active'));
        // Show the selected tab panel
        const targetPanel = document.getElementById(this.dataset.tab);
        targetPanel.classList.add('active');
    });
});
let ascending = true;

function sortTable(tableId, columnIndex) {
    const table = document.getElementById(tableId);
    if (!table || !table.tBodies.length) return; // Ensure table exists and has a tbody

    const rows = Array.from(table.tBodies[0].rows);
    const sortFunction = (a, b) => {
        let valA = a.cells[columnIndex].textContent.trim();
        let valB = b.cells[columnIndex].textContent.trim();

        // Parse as numbers or dates if necessary
        if (!isNaN(valA) && !isNaN(valB)) {
            valA = parseFloat(valA);
            valB = parseFloat(valB);
        } else if (columnIndex === 4) { // Assuming column 4 is the date
            valA = new Date(valA);
            valB = new Date(valB);
        }

        if (valA < valB) return ascending ? -1 : 1;
        if (valA > valB) return ascending ? 1 : -1;
        return 0;
    };

    rows.sort(sortFunction);

    // Re-append sorted rows to the table
    rows.forEach(row => table.tBodies[0].appendChild(row));

    // Toggle sorting order for next click
    ascending = !ascending;
}
