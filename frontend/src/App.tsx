import React, { useState, useEffect } from "react";

type User = {
  id: number;
  first_name: string;
  last_name: string;
  email: string;
};

function App() {
  const [users, setUsers] = useState<User[]>([]);
  const [form, setForm] = useState({
    first_name: "",
    last_name: "",
    email: "",
    password: "",
  });

  useEffect(() => {
    fetch("http://localhost:5000/users")
      .then((res) => res.json())
      .then(setUsers);
  }, []);

  function handleChange(e: React.ChangeEvent<HTMLInputElement>) {
    setForm({ ...form, [e.target.name]: e.target.value });
  }

  function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    fetch("http://localhost:5000/users", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(form),
    }).then(() => {
      setForm({ first_name: "", last_name: "", email: "", password: "" });
      fetch("http://localhost:5000/users")
        .then((res) => res.json())
        .then(setUsers);
    });
  }

  return (
    <div>
      <h1>Inscription</h1>
      <form onSubmit={handleSubmit}>
        <input
          name="first_name"
          value={form.first_name}
          onChange={handleChange}
          placeholder="Prénom"
          required
        />
        <input
          name="last_name"
          value={form.last_name}
          onChange={handleChange}
          placeholder="Nom"
          required
        />
        <input
          name="email"
          value={form.email}
          onChange={handleChange}
          type="email"
          placeholder="Email"
          required
        />
        <input
          name="password"
          value={form.password}
          onChange={handleChange}
          type="password"
          placeholder="Mot de passe"
          required
        />
        <button type="submit">S'inscrire</button>
      </form>

      <h2>Utilisateurs</h2>
      <ul>
        {users.map((u) => (
          <li key={u.id}>
            {u.first_name} {u.last_name} — {u.email}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
