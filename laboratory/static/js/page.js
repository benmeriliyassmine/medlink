
    (function() {
        function buildCalendar() {
            const today = new Date();
            const currentMonth = today.getMonth();
            const currentYear = today.getFullYear();
            const currentDay = today.getDate();


            
            const monthNames = [
                "janv", "fevr", "mars", "avr", "mai", "juin",
                "juil", "aout", "sept", "oct", "nov", "dec"
            ];
            const monthName = monthNames[currentMonth];
            document.getElementById('monthYear').innerText = `${monthName} ${currentYear}`;



            const firstDay = new Date(currentYear, currentMonth, 1).getDay(); 
            // عدد أيام الشهر
            const daysInMonth = new Date(currentYear, currentMonth + 1, 0).getDate();
        
            let offset = (firstDay === 0) ? 6 : firstDay - 1; 


            let tbody = document.getElementById('calendarBody');
            tbody.innerHTML = ''; 


            let row = document.createElement('tr');
            let dayCount = 1;


       
            for (let i = 0; i < 42; i++) {
                if (i % 7 === 0 && i !== 0) {
                    tbody.appendChild(row);
                    row = document.createElement('tr');
                }


                let cell = document.createElement('td');
                if (i >= offset && dayCount <= daysInMonth) {
                    cell.textContent = dayCount;
                 
                    if (dayCount === currentDay) {
                        cell.style.backgroundColor = '#d9ecfa';
                        cell.style.fontWeight = '700';
                        cell.style.color = '#0b4b6b';
                        cell.style.borderRadius = '30px';
                    }
                    dayCount++;
                } else {
                   
                    cell.textContent = '';
                }
                row.appendChild(cell);
            }
            tbody.appendChild(row);



            let rows = tbody.querySelectorAll('tr');
            if (rows.length > 0) {
                let lastRow = rows[rows.length - 1];
                let empty = true;
                for (let cell of lastRow.cells) {
                    if (cell.textContent.trim() !== '') {
                        empty = false;
                        break;
                    }
                }
                if (empty) {
                    lastRow.remove();
                }
            }
        }


        buildCalendar();
    })();