<template>
  <div>
    <v-navigation-drawer v-model="drawer" app>
      <v-sheet color="grey lighten-4" class="pa-5">
        <div>{{ auth.name }}</div>
      </v-sheet>
      <v-divider></v-divider>
      <v-list>
        <v-list-item link>
          <v-list-item-icon>
            <v-icon>mdi-calendar-edit</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>日報を書く</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link>
          <v-list-item-icon>
            <v-icon>mdi-text-box-plus</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>目標を書く</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item to="/tag/create">
          <v-list-item-icon>
            <v-icon>mdi-tag</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>タグを作成する</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item to="/">
          <v-list-item-icon>
            <v-icon>mdi-home</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>ホーム</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link @click="logout">
          <v-list-item-icon>
            <v-icon>mdi-logout</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>ログアウト</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar app color="deep-purple accent-4" dark>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>自己管理アプリ</v-toolbar-title>
    </v-app-bar>
  </div>
</template>

<script>
export default {
  data() {
    return {
      drawer: true,
      auth: [],
    };
  },
  mounted() {
    this.auth = JSON.parse(sessionStorage.getItem("user"));
  },
  methods: {
    logout() {
      sessionStorage.removeItem("user");
      this.$router.push("/login");
    },
  },
};
</script>