import ResourceList from "./components/ResourceList";
import ReservationForm from "./components/ReservationForm";
import ReservationList from "./components/ReservationList";
import "./index.css";

function App() {
return (
<div className="container">
<h1>System Zarzadzania Rezerwacjami</h1>
<ReservationForm />
<ResourceList />
<ReservationList />
</div>
);
}

export default App;