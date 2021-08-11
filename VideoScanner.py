from google.cloud import videointelligence_v1p3beta1 as videointelligence
import io
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="cloudcreds.json"

def videoscanner(path):
    client = videointelligence.StreamingVideoIntelligenceServiceClient()

    # Set streaming config.
    config = videointelligence.StreamingVideoConfig(
        feature=(
            videointelligence.StreamingFeature.STREAMING_EXPLICIT_CONTENT_DETECTION
        )
    )

    # config_request should be the first in the stream of requests.
    config_request = videointelligence.StreamingAnnotateVideoRequest(
        video_config=config
    )

    # Set the chunk size to 5MB (recommended less than 10MB).
    chunk_size = 5 * 1024 * 1024

    # Load file content.
    stream = []
    with io.open(path, "rb") as video_file:
        while True:
            data = video_file.read(chunk_size)
            if not data:
                break
            stream.append(data)

    def stream_generator():
        yield config_request
        for chunk in stream:
            yield videointelligence.StreamingAnnotateVideoRequest(input_content=chunk)

    requests = stream_generator()

    # streaming_annotate_video returns a generator.
    # The default timeout is about 300 seconds.
    # To process longer videos it should be set to
    # larger than the length (in seconds) of the stream.
    responses = client.streaming_annotate_video(requests, timeout=900)

    # Each response corresponds to about 1 second of video.
    for response in responses:
        # Check for errors.
        if response.error.message:
            print(response.error.message)
            break

        for frame in response.annotation_results.explicit_annotation.frames:
            time_offset = (
                frame.time_offset.seconds + frame.time_offset.microseconds / 1e6
            )
            pornography_likelihood = videointelligence.Likelihood(
                frame.pornography_likelihood
            )

            print("Time: {}s".format(time_offset))
            print("\tpornogaphy: {}".format(pornography_likelihood.name))

            return "pornogaphy: {}".format(pornography_likelihood.name)