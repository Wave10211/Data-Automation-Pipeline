const API = "/ingest/todos"; // proxied or absolute

async function load() {
  const res = await fetch(API);
  const data = await res.json();
  const list = document.getElementById("list");
  list.innerHTML = "";
  data.forEach(t => {
    const li = document.createElement("li");
    li.textContent = `${t.id} — ${t.title} — ${t.completed ? "✔" : "✖"} (${t.fetched_at})`;
    list.appendChild(li);
  });
}

document.getElementById("refresh").addEventListener("click", load);
load();
