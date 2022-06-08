<template>
  <div>
    <hello-world />
    <button @click="get">ssss</button>
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
    async get() {
      const data = await this.axios
        .get("http://0.0.0.0:8000/api/tag/index/")
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
