<template>
  <v-app id="inspire">
    <AppBar />
    <v-main class="grey lighten-2">
      <v-container>
        <h1>目標一覧</h1>
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
                <tr v-for="target in targets" :key="target.id">
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
                      :to="{
                        name: 'EditTarget',
                        params: { targetId: target.id },
                      }"
                      style="text-decoration: none"
                    >
                      <v-icon color="green darken-2">mdi-pencil</v-icon>
                    </router-link>
                    <v-icon
                      color="red darken-2"
                      @click="deleteTarget(target.id, target)"
                      >mdi-delete</v-icon
                    >
                  </td>
                </tr>
              </tbody>
            </template>
          </v-simple-table>
        </v-container>
        <h1>達成割合</h1>
        <TargetGraph
          :height="this.height"
          :width="this.width"
          :completedTargetCount="this.completedTargetCount"
          :inCompletedTargetCount="this.inCompletedTargetCount"
          ref="targetGraph"
        >
        </TargetGraph>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import AppBar from "../../components/layouts/AppBar.vue";
import TargetGraph from "../../components/TargetGraph.vue";

export default {
  name: "TargetList",
  components: {
    AppBar,
    TargetGraph,
  },
  data() {
    return {
      auth: [],
      accessToken: null,
      targets: [],
      completedTargetCount: null,
      inCompletedTargetCount: null,
      width: 200,
      height: 100,
    };
  },
  mounted() {
    this.auth = JSON.parse(sessionStorage.getItem("user"));
    this.accessToken = this.auth.accessToken;
    this.getTargets();
  },
  methods: {
    async getTargets() {
      await this.axios
        .get("http://0.0.0.0:8000/api/target_management/index/", {
          headers: { Authorization: "JWT " + this.accessToken },
        })
        .then((response) => {
          this.targets = response.data;
          if (this.targets.length) {
            // 完了済みの目標をカウントする
            const completedTargets = this.targets.filter((value) => {
              return value.status === true;
            });
            this.completedTargetCount = completedTargets.length;
            // 未完了の目標をカウントする
            const inCompletedTargets = this.targets.filter((value) => {
              return value.status === false;
            });
            this.inCompletedTargetCount = inCompletedTargets.length;
            // 子コンポーネントのグラフを再描画する
            this.$refs.targetGraph.createChart();
          } else {
            console.log("ソートしません！");
          }
        })
        .catch((e) => {
          console.log("エラー", e);
        });
    },
    async deleteTarget(targetId, target) {
      console.log("click!");
      await this.axios
        .delete(`http://0.0.0.0:8000/api/target_management/${targetId}/`, {
          headers: { Authorization: "JWT " + this.accessToken },
        })
        .then((response) => {
          console.log(response);
          let index = this.targets.indexOf(target);
          this.targets.splice(index, 1);
        })
        .catch((e) => {
          console.log("目標削除に失敗しました", e);
        });
    },
  },
};
</script>