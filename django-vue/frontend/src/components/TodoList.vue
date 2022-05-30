<template>
  <di>
    <h1>Todos</h1>
    <ul>
      <li v-for="todo of todos" :key="todo.id">
        {{ todo.id }}
      </li>
    </ul>
  </di>
</template>

<script>
import axios from "axios";

export default {
  name: "TodoList",
  data() {
    return {
      todos: []
    };
  },
  async created() {
    try {
      const res = await axios.get(`http://127.0.0.1:8000/api/v2/usdrub/?format=json`);

      this.todos = res.data;
    } catch (e) {
      console.error(e);
    }
  }
};
</script>

<style scoped>
h1 {
  text-decoration: underline;
}

li {
  color: white;
}
</style>
