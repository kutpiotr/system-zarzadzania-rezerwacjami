import { useState } from "react";
import api from "../api";

function ReservationForm() {
const [formData, setFormData] = useState({
start_time: "",
end_time: "",
user_id: "",
resource_id: ""
});

const [message, setMessage] = useState("");

const handleChange = (e) => {
setFormData({
...formData,
[e.target.name]: e.target.value
});
};

const handleSubmit = async (e) => {
e.preventDefault();

try {
await api.post("/reservations/", {
start_time: formData.start_time,
end_time: formData.end_time,
user_id: Number(formData.user_id),
resource_id: Number(formData.resource_id)
});

setMessage("Rezerwacja dodana");
setFormData({
start_time: "",
end_time: "",
user_id: "",
resource_id: ""
});
} catch (error) {
if (error.response && error.response.data && error.response.data.detail) {
setMessage(error.response.data.detail);
} else {
setMessage("Wystapil blad");
}
}
};

return (
<div>
<h2>Dodaj rezerwacje</h2>
<form onSubmit={handleSubmit}>
<div>
<label>Start:</label>
<input
type="datetime-local"
name="start_time"
value={formData.start_time}
onChange={handleChange}
required
/>
</div>

<div>
<label>Koniec:</label>
<input
type="datetime-local"
name="end_time"
value={formData.end_time}
onChange={handleChange}
required
/>
</div>

<div>
<label>User ID:</label>
<input
type="number"
name="user_id"
value={formData.user_id}
onChange={handleChange}
required
/>
</div>

<div>
<label>Resource ID:</label>
<input
type="number"
name="resource_id"
value={formData.resource_id}
onChange={handleChange}
required
/>
</div>

<button type="submit">Dodaj</button>
</form>

{message && <p>{message}</p>}
</div>
);
}

export default ReservationForm;