
#include <stdint.h>
#include <string.h>

#include "noise_suppression.h"

#include "speex/speex_preprocess.h"


class NoiseSuppressionImpl : public NoiseSuppression
{
public:
    NoiseSuppressionImpl(int frame_size=256, int sample_rate=16000);

    ~NoiseSuppressionImpl();

    std::string process(const std::string& near);

private:
    SpeexPreprocessState *st;

    int16_t *e;
    int frames;
};

NoiseSuppression* NoiseSuppression::create(int frame_size, int sample_rate)
{
    return new NoiseSuppressionImpl(frame_size, sample_rate);
}

NoiseSuppressionImpl::NoiseSuppressionImpl(int frame_size, int sample_rate)
{
    // int i;
    // float f;
    st = speex_preprocess_state_init(frame_size, sample_rate);
    frames = frame_size;
    e = new int16_t[frames];

    // i=1;
    // speex_preprocess_ctl(st, SPEEX_PREPROCESS_SET_DENOISE, &i);
    // i=0;
    // speex_preprocess_ctl(st, SPEEX_PREPROCESS_SET_AGC, &i);
    // i=sample_rate;
    // speex_preprocess_ctl(st, SPEEX_PREPROCESS_SET_AGC_LEVEL, &i);
    // i=0;
    // speex_preprocess_ctl(st, SPEEX_PREPROCESS_SET_DEREVERB, &i);
    // f=0.0f;
    // speex_preprocess_ctl(st, SPEEX_PREPROCESS_SET_DEREVERB_DECAY, &f);
    // f=0.0f;
    // speex_preprocess_ctl(st, SPEEX_PREPROCESS_SET_DEREVERB_LEVEL, &f);
}

NoiseSuppressionImpl::~NoiseSuppressionImpl()
{
    speex_preprocess_state_destroy(st);
    delete e;
}

std::string NoiseSuppressionImpl::process(const std::string& near)
{
    const int16_t *y = (const int16_t *)(near.data());
    memcpy(e, y, sizeof(int16_t)*frames);
    speex_preprocess_run(st, e);

    return std::string((const char *)e, frames * sizeof(int16_t));
}

