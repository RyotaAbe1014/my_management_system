<template>
  <div>
    <hello-world />
    <button @click="getIp">ssss</button>
  </div>
</template>

<script>
import HelloWorld from "../components/HelloWorld";
export default {
  name: "TopPage",

  components: {
    HelloWorld,
  },
  methods: {
    async getIp() {
      const data = await this.axios
        .get("http://0.0.0.0:8000/api/book/")
        .then((response) => {
          console.log(response);
        })
        .catch((e) => {
          console.log("エラー", e);
        });
        console.log(data);
    },
  },
};
</script>
