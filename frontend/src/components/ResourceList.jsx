import { useEffect, useState } from "react";
import api from "../api";

function ResourceList() {
const [resources, setResources] = useState([]);

useEffect(() => {
fetchResources();
}, []);

const fetchResources = async () => {
try {
const response = await api.get("/resources/");
setResources(response.data);
} catch (error) {
console.error("Blad podczas pobierania zasobow:", error);
}
};

return (
<div>
<h2>Zasoby</h2>
<ul>
{resources.map((resource) => (
<li key={resource.id}>
{resource.name} - {resource.type}
</li>
))}
</ul>
</div>
);
}

export default ResourceList;