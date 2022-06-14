<template>
  <v-app id="inspire">
    <AppBar />
    <v-main class="grey lighten-2">
      <v-container>
        <h1>完了済み目標一覧</h1>
        <v-container>
          <v-simple-table fixed-header height="600px">
            <template v-slot:default>
              <thead>
                <tr>
                  <th class="text-left">目標</th>
                  <th class="text-left">完了日</th>
                  <th class="text-left">ステータス</th>
                  <th class="text-left">action</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="target in completedTargets" :key="target.id">
                  <td>{{ target.name }}</td>
                  <td>{{ target.completed_at }}</td>
                  <td v-if="target.status == false">
                    <v-icon color="red darken-2">mdi-close-outline</v-icon>
                  </td>
                  <td v-if="target.status == true">
                    <v-icon color="green darken-2">mdi-check-outline</v-icon>
                  </td>
                  <td>
                    <router-link
                      :to="{ name: 'EditTarget', params: { targetId: target.id } }"
                      style="text-decoration: none"
                    >
                    <v-icon color="green darken-2">mdi-pencil</v-icon>
                    </router-link>
                    <v-icon color="red darken-2">mdi-delete</v-icon>
                  </td>
                </tr>
              </tbody>
            </template>
          </v-simple-table>
        </v-container>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import AppBar from "../../components/layouts/AppBar.vue";
export default {
  name: "CompletedTargetList",
  components: {
    AppBar,
  },
  data() {
    return {
      auth: [],
      accessToken: null,
      completedTargets: [],
    };
  },
  mounted() {
    this.auth = JSON.parse(sessionStorage.getItem("user"));
    this.accessToken = this.auth.accessToken;
    this.getCompletedTargets();
  },
  methods: {
    async getCompletedTargets() {
      await this.axios
        .get("http://0.0.0.0:8000/api/target_management/completed/", {
          headers: { Authorization: "JWT " + this.accessToken },
        })
        .then((response) => {
          this.completedTargets = response.data;
          console.log(this.completedTargets);
        })
        .catch((e) => {
          console.log("エラー", e);
        });
    },
  },
};
</script>