<template>
  <div id="app">
    <h1>Task Monitor</h1>
    <div class="task-container">
      <table>
        <tr>
          <th>Name</th>
          <th>Duration (ms)</th>
          <th>State</th>
          <th>&nbsp;</th>
        </tr>
        <TaskMonitor name="First task" />
      </table>
    </div>
  </div>
</template>

<script>
// Vue component modules.
import TaskMonitor from "./components/task_monitor.vue";

export default {
  name: "App",
  components: { TaskMonitor },
};
</script>

<style scoped>
h1 {
  padding-top: 1rem;
}

table {
  border-collapse: collapse;
  width: 100%;
}

.task-container {
  background-color: var(--main-window-white);
  box-shadow: 0 2px 4px 0 rgb(0 0 0 / 10%);
  width: 60%;
  min-width: 800px;
  margin: 0 auto;
  border-radius: 5px;
  padding: 0.5rem;
}
</style>