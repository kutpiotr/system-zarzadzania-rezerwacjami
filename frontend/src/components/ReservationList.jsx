import { useEffect, useState } from "react";
import api from "../api";

function ReservationList() {
const [reservations, setReservations] = useState([]);

useEffect(() => {
fetchReservations();
}, []);

const fetchReservations = async () => {
try {
const response = await api.get("/reservations/");
setReservations(response.data);
} catch (error) {
console.error("Blad podczas pobierania rezerwacji:", error);
}
};

return (
<div>
<h2>Rezerwacje</h2>
<ul>
{reservations.map((reservation) => (
<li key={reservation.id}>
Uzytkownik ID: {reservation.user_id} | Zasob ID: {reservation.resource_id} | {reservation.start_time} - {reservation.end_time} | Status: {reservation.status}
</li>
))}
</ul>
</div>
);
}

export default ReservationList;