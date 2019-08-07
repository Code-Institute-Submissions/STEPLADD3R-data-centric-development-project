'use strict';

var gulp = require( 'gulp' );
var sass = require( 'gulp-sass' );
var uglifycss = require( 'gulp-uglifycss' );

sass.compiler = require('node-sass');

gulp.task('dependencies', function(done) {
    // gulp.src('./node_modules/bootstrap/dist/css/bootstrap.min.css')
        // .pipe(gulp.dest('./static/dist/css/'));
        
    gulp.src('./node_modules/jquery/dist/jquery.slim.min.js')
        .pipe(gulp.dest('./static/dist/js/'));
    
    gulp.src('./node_modules/popper.js/dist/popper.min.js')
        .pipe(gulp.dest('./static/dist/js/'));
    
    gulp.src('./node_modules/bootstrap/dist/js/bootstrap.min.js')
        .pipe(gulp.dest('./static/dist/js/'));

    done();
});

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
        .pipe(gulp.dest('./static/dist/css/'));

    done();
});

gulp.task('run', gulp.series('sass', 'uglify'));

gulp.task('watch', function() {
    gulp.watch('./static/scss/*.scss', gulp.series('sass'));
    gulp.watch('./static/css/*.css', gulp.series('uglify'));
});

gulp.task('default', gulp.series('run', 'watch'));