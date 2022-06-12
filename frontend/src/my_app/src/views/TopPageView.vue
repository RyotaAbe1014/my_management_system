<template>
  <v-app id="inspire">
    <AppBar />
    <v-main class="grey lighten-2">
      <v-container>
        <h1>dashboard</h1>
        <v-row>
          <template>
            <v-col class="mt-2" cols="12">
              <strong>日報</strong>
            </v-col>
            <v-col cols="6" md="2">
              <v-card class="mx-auto" max-width="344" height="150">
                <v-card-text>
                  <p class="text-h5 text--primary">日報作成</p>
                </v-card-text>
                <v-card-actions>
                  <router-link
                    to="daily_report/create"
                    class="mx-auto"
                    style="text-decoration: none"
                  >
                    <v-btn class="mx-auto" outlined color="primary"> GO </v-btn>
                  </router-link>
                </v-card-actions>
              </v-card>
            </v-col>
            <v-col cols="6" md="2">
              <v-card class="mx-auto" max-width="344" height="150">
                <v-card-text>
                  <p class="text-h5 text--primary">日報一覧</p>
                </v-card-text>
                <v-card-actions>
                  <router-link
                    to="daily_report"
                    class="mx-auto"
                    style="text-decoration: none"
                  >
                    <v-btn class="mx-auto" outlined color="primary"> GO </v-btn>
                  </router-link>
                </v-card-actions>
              </v-card>
            </v-col>
            <v-col cols="6" md="2">
              <v-card class="mx-auto" max-width="344" height="150">
                <v-card-text>
                  <p class="text-h5 text--primary">日報検索</p>
                </v-card-text>
                <v-card-actions>
                  <v-btn class="mx-auto" outlined color="primary"> GO </v-btn>
                </v-card-actions>
              </v-card>
            </v-col>
          </template>
          <template>
            <v-col class="mt-2" cols="12">
              <strong>目標管理</strong>
            </v-col>
            <v-col cols="6" md="2">
              <v-card class="mx-auto" max-width="344" height="150">
                <v-card-text>
                  <p class="text-h5 text--primary">目標作成</p>
                </v-card-text>
                <v-card-actions>
                  <router-link
                    to="target/create"
                    class="mx-auto"
                    style="text-decoration: none"
                  >
                    <v-btn class="mx-auto" outlined color="primary"> GO </v-btn>
                  </router-link>
                </v-card-actions>
              </v-card>
            </v-col>
            <v-col cols="6" md="2">
              <v-card class="mx-auto" max-width="344" height="150">
                <v-card-text>
                  <p class="text-h5 text--primary">目標一覧</p>
                </v-card-text>
                <v-card-actions>
                  <router-link
                    to="target"
                    class="mx-auto"
                    style="text-decoration: none"
                  >
                    <v-btn class="mx-auto" outlined color="primary"> GO </v-btn>
                  </router-link>
                </v-card-actions>
              </v-card>
            </v-col>
            <v-col cols="6" md="2">
              <v-card class="mx-auto" max-width="344" height="150">
                <v-card-text>
                  <p class="text-h5 text--primary">達成済一覧</p>
                </v-card-text>
                <v-card-actions>
                  <v-btn class="mx-auto" outlined color="primary"> GO </v-btn>
                </v-card-actions>
              </v-card>
            </v-col>
          </template>
          <template>
            <v-col class="mt-2" cols="12">
              <strong>タグ管理</strong>
            </v-col>
            <v-col cols="6" md="2">
              <v-card class="mx-auto" max-width="344" height="150">
                <v-card-text>
                  <p class="text-h5 text--primary">タグ作成</p>
                </v-card-text>
                <v-card-actions>
                  <router-link
                    to="tag/create"
                    class="mx-auto"
                    style="text-decoration: none"
                  >
                    <v-btn class="mx-auto" outlined color="primary"> GO </v-btn>
                  </router-link>
                </v-card-actions>
              </v-card>
            </v-col>
            <v-col cols="6" md="2">
              <v-card class="mx-auto" max-width="344" height="150">
                <v-card-text>
                  <p class="text-h5 text--primary">タグ一覧</p>
                </v-card-text>
                <v-card-actions>
                  <router-link
                    to="tag"
                    class="mx-auto"
                    style="text-decoration: none"
                  >
                    <v-btn class="mx-auto" outlined color="primary"> GO </v-btn>
                  </router-link>
                </v-card-actions>
              </v-card>
            </v-col>
          </template>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import AppBar from "../components/layouts/AppBar.vue";
export default {
  name: "TopPage",
  components: {
    AppBar,
  },
};
</script>
