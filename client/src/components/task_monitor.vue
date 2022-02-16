<template>
  <tr>
    <td>{{ name }}</td>
    <td><input type="number" v-model="time" /></td>
    <td>{{ state }}</td>
    <td><button @click="onClick">Begin</button></td>
  </tr>
</template>

<script>
import { getJson, postJson } from "../api.js";

export default {
  name: "TaskMonitor",
  props: {
    name: {
      type: String,
    },
  },
  data() {
    return {
      time: 3000, // milliseconds.
      state: "Idle",
    };
  },
  methods: {
    async onClick() {
      const response = await postJson("/api/start_task", {
        name: this.name,
        time: this.time,
      });

      this.state = response.state;
      this.getTaskStatus(response.task_id);
    },
    async getTaskStatus(task_id) {
      const response = await getJson(`/api/task_status/${task_id}`);

      console.log(`response: ${JSON.stringify(response)}`);
      this.state = response.status;

      if (response.state === "PROGRESS") {
        setTimeout(() => {
          this.getTaskStatus(task_id);
        }, 1000);
      }
    },
  },
};
</script>

<style scoped>
tr {
  align-items: center;
  border-bottom: var(--border-grey) 1px solid;
}
td {
  margin: 0 1rem;
  padding: 0.25rem 2rem;
}

button {
  background-color: var(--control-colour);
  cursor: pointer;
  color: white;
  font-size: var(--control-font-size);
  padding: 4px 20px;
  border: none;
  border-radius: 5px;
}
button:hover {
  opacity: 0.8;
}
.button:active {
  background-color: var(--mid-blue);
}
.button:focus {
  box-shadow: 0 0 3pt 2pt var(--mid-blue);
  outline: none;
}
.button.disabled {
  opacity: 0.3;
  pointer-events: none;
}
</style>