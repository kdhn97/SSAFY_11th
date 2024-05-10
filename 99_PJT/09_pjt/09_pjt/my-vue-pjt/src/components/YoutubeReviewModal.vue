<template>
  <!-- 모달 컴포넌트 -->
  <div class="modal" v-if="modalOn" @click="ModalClick">
    <div class="modal-content" @click.stop>
      <!-- 닫기 버튼 -->
      <button @click="modalOff">x</button>
      <!-- 비디오 제목 -->
      <div class="modal-title">{{ video.snippet.title }}</div>
      <!-- 비디오 임베드 -->
      <div class="modal-body">
        <iframe width="560" height="315" :src="videoUrl" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, defineEmits, defineProps } from 'vue'

// 사용자 정의 이벤트 정의
const emit = defineEmits(['modalOff'])

// 컴포넌트를 위한 props 정의
const props = defineProps({
  video: Object,
  modalOn: Boolean
})

// 비디오 URL을 생성하기 위한 계산된 속성
const videoUrl = computed(() => {
  if (props.video) {
    return `https://www.youtube.com/embed/${props.video.id.videoId}`
  }
})

// 모달을 닫는 함수
const modalOff = function () {
  emit('modalOff')
}

// 모달 클릭 처리 함수
const ModalClick = function (event) {
  if (event.target.classList.contains('modal')) {
    modalOff()
  }
}
</script>

<style scoped>
/* 모달에 대한 스타일링 */
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color:rgba(0, 0, 0, 0.205);
  display: flex;
  align-items: center;
  justify-content: center;
}

/* 모달 내용에 대한 스타일링 */
.modal-content {
  background-color: #fff;
  padding: 20px;
  border-radius: 8px;
  max-width: 80%;
  max-height: 80%;
  overflow-y: auto; 
}

/* 모달 제목에 대한 스타일링 */
.modal-title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 10px;
}

/* 모달 본문에 대한 스타일링 */
.modal-body {
  font-size: 16px;
}
</style>
