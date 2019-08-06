'use strict';

var gulp = require( 'gulp' );
var sass = require( 'gulp-sass' );
var uglifycss = require( 'gulp-uglifycss' );

sass.compiler = require('node-sass');

gulp.task('sass', function() {
    return gulp.src('./static/scss/*.scss')
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest('./static/css'));
});

gulp.task('uglify', function(done) {
    gulp.src('./static/css/*.css')
        .pipe(uglifycss({
            'uglyComments': true,
        }))
        .pipe(gulp.dest('./static/dist/'));
    done();
});

gulp.task('run', gulp.series('sass', 'uglify'));

gulp.task('watch', function() {
    gulp.watch('./static/scss/*.scss', gulp.series('sass'));
    gulp.watch('./static/css/*.css', gulp.series('uglify'));
});

gulp.task('default', gulp.series('run', 'watch'));